use std::fs;

mod day_01;
mod day_02;
mod util;

fn main() {
  let RESOURCE = "day_01/input_01.txt";
  let expenses = util::get_resource(&RESOURCE);
  println!("Answer 2 : {}", day_01::expense_anomaly_triple(&expenses));


  // match fs::read_to_string("../resources/day_01/input_01.txt") {
  //   Ok(expenses) => {
  //     println!("Answer 1 : {}", day_01::expense_anomaly(&expenses));
  //     println!("Answer 2 : {}", day_01::expense_anomaly_triple(&expenses));
  //   }
  //   Err(why) => {
  //     print!("{}", why);
  //   }
  // }

  match fs::read_to_string("../resources/day_02/input.txt") {
    Ok(expenses) => {
      println!("Day 02");
      println!("\tAnswer 1 : {}", day_02::answer_1());
      println!("\tAnswer 2 : {}", day_02::answer_2());
    }
    Err(why) => {
      print!("{}", why);
    }
  }
}
