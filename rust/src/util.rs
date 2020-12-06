use std::fs;

pub fn get_resource(name: &str) -> Split<String> {
  match fs::read_to_string("../resources/".to_owned() + name) {
    Ok(lines) => {
      return lines.split("\n");
    }
    Err(why) => {
      eprint!("{}", why);
    }
  }
}
