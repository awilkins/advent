use std::fs;
use std::env;
use std::io;

pub fn get_resource(name: &str) -> io::Result<String> {
  let mut cwd = env::current_dir()?;
  cwd.push("..");
  cwd.push("resources");
  cwd.push(name);
  return fs::read_to_string(cwd);
}
