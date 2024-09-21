mod test;

struct Solution;

use std::collections::HashMap;

impl Solution {
	pub fn group_the_people(group_sizes: Vec<i32>) -> Vec<Vec<i32>> {
		group_sizes.into_iter().enumerate().fold(HashMap::new(), |mut map, (i, size)| {
			map.entry(size).or_insert_with(Vec::new).push(i as i32);
			map
		}).into_iter().map(|(k, v)| {
			let mut res = vec![];
			for i in (0..v.len()).step_by(k as usize) {
				res.push(v[i..i+k as usize].to_vec());
			}
			res
		}).flatten().collect()
	}
}

fn main() {
    println!("Hello, world!");
}
