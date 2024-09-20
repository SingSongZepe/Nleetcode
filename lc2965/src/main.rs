mod test;

struct Solution;

impl Solution {
    pub fn find_missing_and_repeated_values(grid: Vec<Vec<i32>>) -> Vec<i32> {

        let n = grid.len() as i32;
        let tn = n * n;

        let s = tn * (tn + 1) / 2;
        let sqr_s = tn * (tn + 1) * (2 * tn + 1) / 6;

        let (act_s, act_sqr_s) = grid.into_iter().flatten().collect::<Vec<i32>>().into_iter().fold((0, 0), |(act_s, act_sqr_s), x| {
            (act_s + x, act_sqr_s + x * x)
        });

        let diff = act_s - s;
        let diff_sqr = act_sqr_s - sqr_s;

        vec![(diff + diff_sqr / diff) / 2, (diff_sqr / diff - diff) / 2]
    }
}

struct Solution1;

impl Solution1 {
    pub fn find_missing_and_repeated_values(grid: Vec<Vec<i32>>) -> Vec<i32> {
        let n = grid.len() as i64;
        let tn = n * n;

        let s = tn * (tn + 1) / 2;
        let sqr_s = tn * (tn + 1) * (2 * tn + 1) / 6;

        let (act_s, act_sqr_s) = grid.into_iter().flatten().collect::<Vec<i32>>().into_iter().fold((0i64, 0i64), |(act_s, act_sqr_s), x: i32| {
            (act_s + x as i64, act_sqr_s + (x * x) as i64)
        });

        let diff = act_s - s;
        let diff_sqr = act_sqr_s - sqr_s;

        vec![((diff + diff_sqr / diff) / 2) as i32, ((diff_sqr / diff - diff) / 2) as i32]
    }
}

fn main() {
    println!("Hello, world!");
}
