mod test;

struct Solution;

impl Solution {
	pub fn lexical_order(n: i32) -> Vec<i32> {
		let mut result = vec![];

		fn dfs(n: i32, curr: i32, result: &mut Vec<i32>) {
			if curr > n {
				return;
			}
			result.push(curr);
			dfs(n, curr * 10, result);
			if curr % 10 != 9 {
				dfs(n, curr + 1, result);
			}
		}
		dfs(n, 1, &mut result);

		result
	}
}

impl Solution {
	pub fn lexical_order(n: i32) -> Vec<i32> {
		let mut ans = Vec::with_capacity(n as usize);
		let mut cur = 1;
		for _ in 0..n {
			ans.push(cur);
			if cur * 10 <= n {
				cur = cur * 10;
			} else {
				while cur % 10 == 9 || cur >= n {
					cur /= 10;
				}
				cur += 1;
			}
		}
		ans
	}
}

fn main() {
    println!("Hello, world!");
}
