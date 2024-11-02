mod test;

struct Solution;

impl Solution {
	pub fn is_circular_sentence(sentence: String) -> bool {

		sentence.split(" ").into_iter().fold((true, None), |(result, last_char): (bool, Option<u8>), str| {
			let str = str.as_bytes();
			(result && if let Some(char) = last_char {
				char == str[0]
			} else { true } , Some(str[str.len()-1]))
		}).0 && sentence.as_bytes()[0] == sentence.as_bytes()[sentence.len()-1]

	}
}


fn main() {
    println!("Hello, world!");
}
