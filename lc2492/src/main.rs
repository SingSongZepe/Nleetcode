mod test;


use std::collections;
use collections::HashMap;
use collections::HashSet;
use collections::VecDeque;

struct Solution;

// BFS solution
impl Solution {
	pub fn min_score(n: i32, roads: Vec<Vec<i32>>) -> i32 {

		let mut d = HashMap::<i32, Vec::<[i32; 2]>>::new();

		roads.into_iter().for_each(|road| {
			d.entry(road[0]).or_insert(vec![]).push([road[1], road[2]]);
			d.entry(road[1]).or_insert(vec![]).push([road[0], road[2]]);
		});

		let mut dq = VecDeque::from([1]);
		let mut visited = HashSet::<i32>::new();
		let mut min_score = 10000;

		while !dq.is_empty() {
			for i in 0..dq.len() {
				let node = dq.pop_front().unwrap();
				for t in d.get(&node).unwrap() {
					min_score = min_score.min(t[1]);
					if !visited.contains(&t[0]) {
						visited.insert(t[0]);
						dq.push_back(t[0]);
					}
				}
			}
		}

		min_score
	}
}

fn main() {
    println!("Hello, world!");
}
