use std::cmp::min;

mod test;

struct Solution;

impl Solution {
	pub fn count_squares(mut matrix: Vec<Vec<i32>>) -> i32 {

		for i in 1..matrix.len() {
			for j in 1..matrix[0].len() {
				if matrix[i][j] == 1 {
					matrix[i][j] = 1 + min(min(matrix[i-1][j-1], matrix[i][j-1]), matrix[i-1][j]);
				}
			}
		}

		matrix.iter().map(|row| row.iter().sum::<i32>()).sum()
	}
}

fn main() {
    println!("Hello, world!");
}
