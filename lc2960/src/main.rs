mod test;

struct Solution;

impl Solution {
	pub fn count_tested_devices(battery_percentages: Vec<i32>) -> i32 {
		battery_percentages.into_iter().fold(0, |acc, x| {
			if x > acc {
				acc + 1
			} else {
				acc
			}
		})
	}
}

fn main() {
    println!("Hello, world!");
}
