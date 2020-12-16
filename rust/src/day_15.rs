
pub fn next_number(starting_numbers: Vec<usize>, max_count: usize) -> usize {
  let mut count: usize = 0;
  let mut number = vec![0usize; 30_000_000];

  let mut last_number: usize = 0;
  for n in starting_numbers {
    count += 1;
    number[n] = count;
    last_number = n;
  }

  while count < max_count {
    let mut next: usize = 0;
    let n: usize = number[last_number];

    if n != 0 {
      next = count - n;
    }
    number[last_number] = count;
    count += 1;
    last_number = next;
  }

  return last_number;
}

pub fn play(input: String, max_count: usize) -> usize {
  let numbers: Vec<usize> = input.split(',').map(
    |x| match x.parse::<usize>() { Ok(x) => x, Err(_e) => 0}
  ).collect();
  return next_number(numbers, max_count);
}
