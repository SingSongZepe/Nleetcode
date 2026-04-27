use core::num;


struct Solution;

impl Solution {
    pub fn xor_after_queries(nums: Vec<i32>, queries: Vec<Vec<i32>>) -> i32 {
        queries.iter().fold(nums, |mut nums: Vec<i32>, query| {
            (query[0] as usize..=query[1] as usize).step_by(query[2] as usize).for_each(|idx| {
                nums[idx]  = ((nums[idx] as i64 * query[3] as i64) % 1_000_000_007 as i64) as i32;
            });
            nums
        }).iter().fold(0, |acc, num| {
            acc ^ num
        })
    }
}

fn main() {
    println!("Hello, world!");
}
