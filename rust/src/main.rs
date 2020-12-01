use std::fs;

mod day_01;

fn main() {
    match fs::read_to_string("../resources/day_01/input_01.txt") {
        Ok(expenses) => {
            println!("Answer 1 : {}", day_01::expense_anomaly(&expenses));
            println!("Answer 2 : {}", day_01::expense_anomaly_triple(&expenses));
        }
        Err(why) => {
            print!("{}", why);
        }
    }
}
