

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(battery_percentages: Vec<i32>, expected: i32) {
		let result = Solution::count_tested_devices(battery_percentages);
		println!("{:?}", result);
		assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		let battery_percentages = vec![1, 1, 2, 1, 3];
		let expected = 3;
		t(battery_percentages, expected);
	}

	#[test]
	fn test2() {
		let battery_percentages = vec![0, 1, 2];
		let expected = 2;
		t(battery_percentages, expected);
	}
}