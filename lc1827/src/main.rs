mod test;

struct Solution;

impl Solution {
	pub fn min_operations(nums: Vec<i32>) -> i32 {
		if nums.len() == 1 { 0 } else {
			nums.into_iter().fold((0, 0), |(last, sum), num| {
				if num > last {
					(num, sum)
				} else {
					(last + 1, sum + last - num + 1)
				}
			}).1
		}
	}
}

fn main() {
    println!("Hello, world!");
}
