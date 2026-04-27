
struct Solution;
struct Solution1;

impl Solution {
    pub fn check_ones_segment(s: String) -> bool {
        s.chars().fold((false, true), |(zeroed, res), c| {
            if c == '1' {           // c == '1'
                (zeroed, !zeroed)
            } else {                // c == '0'
                (true, res)
            }   
        }).1
    }
}


impl Solution1 {
    pub fn check_ones_segment(s: String) -> bool {
        !s.as_bytes().windows(2).any(|w| w[0] == b'0' && w[1] == b'1')
    }
}

fn main() {
    println!("Hello, world!");
}
