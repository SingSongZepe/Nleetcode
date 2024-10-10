mod test;

struct Solution;

impl Solution {
	pub fn max_width_ramp(nums: Vec<i32>) -> i32 {

		let mut stk: Vec<usize>=  vec![];
		let mut m: i32 = 0;

		for (idx, &n) in nums.iter().enumerate() {
			if stk.is_empty() || n < nums[stk[stk.len() - 1]] {
				stk.push(idx);
			} else {
				let mut p = stk.len() as i32 - 1;
				while p >= 0 && nums[stk[p as usize]] <= n {
					let diff = (idx - stk[p as usize]) as i32;
					if m < diff {
						m = diff;
					}
					p -= 1;
				}
			}
		}

		m
	}
}

fn main() {
    println!("Hello, world!");
}
