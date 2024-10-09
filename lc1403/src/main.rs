mod test;

struct Solution;

impl Solution {
	pub fn min_subsequence(mut nums: Vec<i32>) -> Vec<i32> {
		nums.sort_unstable_by_key(|&v| -v);
		let mut v = vec![];
		let (mut sum, mut tot) = (nums.iter().sum::<i32>(), 0);
		for n in nums {
			tot += n;
			v.push(n);
			if tot > sum - tot {
				break;
			}
		}

		v
	}
}

fn main() {
    println!("Hello, world!");
}
