mod test;

struct Solution;

impl Solution {
	pub fn parse_bool_expr(expression: String) -> bool {
		expression.bytes().into_iter().fold((Vec::new(), Vec::new(), false), |(mut op_stack, mut bool_stack, mut jump), c| {
			if jump {
				(op_stack, bool_stack, jump)
			} else{
				match c {
					b'(' | b',' => { }
					b'&' | b'|' | b'!' => {
						op_stack.push(c);
						bool_stack.push(Vec::new());
					}
					b't' | b'f' => {
						bool_stack.last_mut().unwrap().push(if c == b't' { true} else { false });
						if let Some(&last) = op_stack.last() {
							if (last == b'&' && c == b'f') || last == b'|' && c == b't'  {
								jump = true
							}
						}
					}
					b')' => {
						jump = false;
						if let Some(&last) = op_stack.last() {
							let mut rb = false;
							if let Some(current) = bool_stack.pop() {
								match last {
									b'&' => {
										rb = current.into_iter().all(|x| x);
									}
									b'|' => {
										rb = current.into_iter().any(|x| x);
									}
									_ => {
										rb = ! current[0]
									}
								}
							}
							if !bool_stack.is_empty() {
								bool_stack.last_mut().unwrap().push(rb);
							} else {
								bool_stack.push(Vec::from([rb]));
							}
						}
					}
					_ => { }
				}
				(op_stack, bool_stack, jump)
			}
		}).1[0][0]
	}
}

struct Solution1;

impl Solution1 {
	pub fn parse_bool_expr(expr: String) -> bool {
		let eval = |s: &str| -> bool {
			let mut stack = Vec::new();
			let mut op = None;
			for &b in s.as_bytes() {
				match b {
					b'(' => {
						let start = stack.len();
						while let Some(c) = stack.pop() {
							if c == b')' { break; }
						}
						let sub_expr = &s[start..stack.len()];
						// lambda can not call himself
						// stack.push(if eval(sub_expr) { b't' } else { b'f' });
					}
					b'|' | b'&' | b'!' => op = Some(b),
					b't' => stack.push(b't'),
					b'f' => stack.push(b'f'),
					b')' => if let Some(op) = op {
						let vals: Vec<bool> = stack.iter().map(|&x| x == b't').collect();
						stack.truncate(stack.len() - vals.len()); // Remove evaluated items
						stack.push(match op {
							b'|' => if vals.iter().any(|&v| v) { b't' } else { b'f' },
							b'&' => if vals.iter().all(|&v| v) { b't' } else { b'f' },
							b'!' => if vals[0] { b'f' } else { b't' },
							_ => unreachable!(),
						});
					},
					_ => {}
				}
			}
			stack.last() == Some(&b't')
		};
		eval(&expr)
	}
}

fn main() {
    println!("Hello, world!");
}
