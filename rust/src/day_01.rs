
use std::iter::FromIterator;

pub fn expense_anomaly(expenses: &String) -> i32 {
  let expense_list: Vec<i32> = expenses.split('\n').map(
    |x| match x.parse::<i32>() { Ok(x) => x, Err(_e) => -1}
  ).collect();

  for ii in 0..expense_list.len() {
    for jj in 0..expense_list.len() {
      if ii == jj {
        continue;
      }

      let a = expense_list[ii];
      let b = expense_list[jj];

      if a + b == 2020 {
        return a * b;
      }
    }
  }

  return 0;
}

pub fn expense_anomaly_triple(expenses: &Vec<String>) -> i32 {
  let expense_list = Vec::from_iter(
    expenses.iter().map(|x| match x.parse::<i32>() {
      Ok(x) => x,
      Err(_e) => -1
    })
  );

  for ii in 0..expense_list.len() {
    for jj in 0..expense_list.len() {
      for kk in 0..expense_list.len() {
        if ii == jj || ii == kk || kk == jj {
          continue;
        }

        let a = expense_list[ii];
        let b = expense_list[jj];
        let c = expense_list[kk];

        if a + b + c == 2020 {
          return a * b * c;
        }
      }
    }
  }

  return 0;
}
