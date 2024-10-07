mod test;

struct Solution;

impl Solution {
	pub fn min_length(s: String) -> i32 {
		let mut count = 0;
		let mut stack = vec![];
		for c in s.chars() {
			if c == 'A' {
				stack.push(1);
			} else if c == 'C' {
				stack.push(-1);
			} else if c == 'B' {
				if let Some(&top) = stack.last() {
					if top == 1 {
						count += 1;
						stack.pop();
						continue;
					}
				} stack.push(0);
			} else if c == 'D' {
				if let Some(&top) = stack.last() {
					if top == -1 {
						count += 1;
						stack.pop();
						continue;
					}
				} stack.push(0);
			} else {
				stack.push(0);
			}
 		}

		s.len() as i32 - 2 * count
	}
}

struct Solution1;

impl Solution1 {
	pub fn min_length(s: String) -> i32 {
		s.len() as i32 - 2 * s.bytes().into_iter().fold((0, vec![]), |(mut cnt, mut stack), b| {
			match b {
				b'A' => {
					stack.push(1);
				}
				b'C' => {
					stack.push(-1);
				}
				b'B' => {
					if let Some(top) = stack.last_mut() {
						if *top == 1 {
							stack.pop();
							cnt += 1;
						} else {
							*top = 0;
						}
					} else {
						stack.push(0);
					}
				}
				b'D' => {
					if let Some(top) = stack.last_mut() {
						if *top == -1 {
							stack.pop();
							cnt += 1;
						} else {
							*top = 0;
						}
					} else {
						stack.push(0);
					}
				}
				_ => {
					stack.push(0);
				}
			}
			(cnt, stack)
		}).0
	}
}


struct Solution2;

impl Solution2 {
	pub fn min_length(s: String) -> i32 {
		let stack = s.bytes().fold(vec![], |mut stack, b| {
			if let Some(&top) = stack.last() {
				match (top, b) {
					(b'A', b'B') | (b'C', b'D') => {
						stack.pop();
					} _ => {
						stack.push(b);
					}
				}
			} else {
				stack.push(b);
			}
			stack
		});

		stack.len() as i32 // 返回栈的长度
	}
}

fn main() {
    println!("Hello, world!");
}
