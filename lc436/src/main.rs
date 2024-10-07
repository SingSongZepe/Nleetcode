mod test;

struct Solution;

// O(n^2) time, O(n) space
impl Solution {
	pub fn find_right_interval(intervals: Vec<Vec<i32>>) -> Vec<i32> {
		let mut result = Vec::new();
		for i in 0..intervals.len() {
			result.push(Solution::get_right_interval(i as i32, intervals[i][1], &intervals));
		}
		result
	}

	fn get_right_interval(current_index: i32, end_time: i32, intervals: &Vec<Vec<i32>>) -> i32 {
		let mut sol_index: i32 = -1;
		let mut closest_start_time = i32::MAX;

		for i in 0..intervals.len() {
			if i as i32 == current_index {
				continue;
			}
			let start_time = intervals[i][0];
			if end_time <= start_time && start_time < closest_start_time {
				closest_start_time = start_time;
				sol_index = i as i32;
			}
		}

		sol_index
	}
}

struct Solution1;

// O(nlogn) time, O(n) space
impl Solution1 {
	pub fn find_right_interval(intervals: Vec<Vec<i32>>) -> Vec<i32> {
		let n = intervals.len();
		let mut intervals = intervals.into_iter().enumerate().map(|(i, x)| ([x[0], x[1]], i)).collect::<Vec<_>>();
		intervals.sort_unstable();
		let mut result = vec![-1; n];
		for &([_, end], i) in &intervals {
			if let Ok(idx) | Err(idx) = intervals.binary_search_by_key(&end, |x| x.0[0]) {
				if idx != n { result[i] = intervals[idx].1 as i32; }
			}
		}
		result
	}
}


struct Solution2;

impl Solution2 {
	pub fn find_right_interval(intervals: Vec<Vec<i32>>) -> Vec<i32> {
		if intervals.len() == 1  {
			if intervals[0][0] == intervals[0][1] {
				return Vec::from([0]);
			}

			return Vec::from([-1]);
		}

		let n = intervals.len();

		let mut dict : Vec<(i32, i32)> = Vec::new();
		let mut result = Vec::new();

		for i in 0..n {
			dict.push((intervals[i][0], i as i32));
			result.push(-1);
		}

		dict.sort_by(|a,b| a.0.cmp(&b.0));

		for i in 0..n {
			// let mut (h,l) = ()
			let mut up = n - 1;
			let mut low = 0;

			let (mut l, mut h) = (0, n - 1);

			while low <= up {
				let m = (l + (h - l) / 2);

				if m > n - 1 {
					break;
				}

				if dict[m].0 >= intervals[i][1] {
					result[i] = dict[m].1;
					h = m - 1;
				} else {
					l = m + 1;
				}

			}
		}
		result
	}
}


fn main() {
    println!("Hello, world!");
}
