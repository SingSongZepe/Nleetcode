mod test;

struct Solution;

impl Solution {
	pub fn subtract_product_and_sum(mut n: i32) -> i32 {
		let (mut product, mut sum) = (1, 0);
		while n > 0 {
			product *= n % 10;
			sum += n % 10;
			n /= 10;
		}
		product - sum
	}
}

struct Solution1;

impl Solution1 {
	pub fn subtract_product_and_sum(n: i32) -> i32 {
		// product
		n.to_string().chars()
			.map(|x| x.to_digit(10).unwrap() as i32)
			.collect::<Vec<i32>>()
			.into_iter()
			.product::<i32>()
			// sum
			- n.to_string().chars()
			.map(|x| x.to_digit(10).unwrap() as i32)
			.collect::<Vec<i32>>()
			.into_iter()
			.sum::<i32>()
	}
}

fn main() {
    println!("Hello, world!");
}
