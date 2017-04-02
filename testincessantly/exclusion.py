import fnmatch

def parse_pattern_file(file):
  stripped_lines = (line.strip() for line in file)
  return set(line for line in stripped_lines if line and not line.startswith('#'))

def exclude_paths_matching_patterns(paths, patterns):
  return set(
    path for path in paths
    if not any(fnmatch.fnmatch(path, pattern) for pattern in patterns))
