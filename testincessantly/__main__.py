#!/usr/bin/python

import logging
import subprocess
import argparse
import argparse

import testincessantly

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', action='store_true')
parser.add_argument('-e', '--exclude-pattern', action='append', help='glob to ignore filepaths matching')
parser.add_argument('--exclude-pattern-file', help='file containing globs to ignore filepaths matching, one per line')
parser.add_argument('--kill-timeout', type=float, help='wait up to [timeout] seconds for test process to terminate before `kill -9`ing it')
parser.add_argument('target_directory')
parser.add_argument('test_command', nargs='+')

def main():
  args = parser.parse_args()

  if args.verbose:
    logging.basicConfig(level=logging.DEBUG)

  bad_patterns = set(args.exclude_pattern)
  if args.exclude_pattern_file is not None:
    bad_patterns.update(testincessantly.exclusion.parse_pattern_file(open(args.exclude_pattern_file)))

  try:
    with testincessantly.RestartableProcess(args.test_command, stdin=subprocess.DEVNULL) as test_process:
      for paths in testincessantly.debounce(testincessantly.iter_modified_file_paths(args.target_directory), delay=0.1):
        paths = testincessantly.exclusion.exclude_paths_matching_patterns(paths, bad_patterns)
        if paths:
          test_process.restart()
  except KeyboardInterrupt:
    pass
