
mod day_01;
mod day_02;
mod day_15;
mod util;

fn main() {
  const RESOURCE: &str = "day_15/input.txt";
  match util::get_resource(RESOURCE) {
    Ok(input) => {
      println!("Day 15");
      println!("\tAnswer 2 : {}", day_15::play("2,0,1,9,5,19".to_owned(), 30_000_000));
    }
    Err(why) => {
      eprint!("{}", why);
    }
  }
  // println!("Answer 2 : {}", day_01::expense_anomaly_triple(&expenses));


  // match fs::read_to_string("../resources/day_01/input_01.txt") {
  //   Ok(expenses) => {
  //     println!("Answer 1 : {}", day_01::expense_anomaly(&expenses));
  //     println!("Answer 2 : {}", day_01::expense_anomaly_triple(&expenses));
  //   }
  //   Err(why) => {
  //     print!("{}", why);
  //   }
  // }

  // match fs::read_to_string(input) {
  //   Ok(input) => {
  //     println!("Day 15");
  //     // println!("\tAnswer 1 : {}", day_02::answer_1());
  //     println!("\tAnswer 2 : {}", day_15::play(input, 30_000_000));
  //   }
  //   Err(why) => {
  //     print!("{}", why);
  //   }
  // }
}
