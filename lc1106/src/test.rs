

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(arg: String, expected: bool) {
		let result = Solution::parse_bool_expr(arg);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}

	fn t1(arg: String, expected: bool) {
		let result = Solution1::parse_bool_expr(arg);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let expression = String::from("&(|(f))");
		let expected = false;
		t(expression, expected);
	}

	#[test]
	fn test2() {
		let expression = String::from("|(f,f,f,t)");
		let expected = true;
		t(expression, expected);
	}

	#[test]
	fn test3() {
		let expression = String::from("!(&(f,t))");
		let expected = true;
		t(expression, expected);
	}



	#[test]
	fn test11() {
		let expression = String::from("&(|(f))");
		let expected = false;
		t1(expression, expected);
	}

	#[test]
	fn test21() {
		let expression = String::from("|(f,f,f,t)");
		let expected = true;
		t1(expression, expected);
	}

	#[test]
	fn test31() {
		let expression = String::from("!(&(f,t))");
		let expected = true;
		t1(expression, expected);
	}

}