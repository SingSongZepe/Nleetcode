mod test;

struct Solution;use std::collections::HashSet;

impl Solution {
	pub fn uncommon_from_sentences(s1: String, s2: String) -> Vec<String> {
		// let mut st1 = HashSet::<String>::new();
		// let mut st2 = HashSet::<String>::new();

		let (s1, s2) = s1.split_whitespace().into_iter()
			.chain(s2.split_whitespace().into_iter())
			.fold((HashSet::<&str>::new(), HashSet::<&str>::new()),
				  |(mut st1, mut st2), word| {
					  if st1.contains(word) {
						  st2.insert(word);
					  } else {
						  st1.insert(word);
					  } (st1, st2)
				  });

		// get word that in s1 but not in s2 into Vec<String>
		s1.into_iter().filter(|word| !s2.contains(word)).map(|word| word.to_string()).collect()
	}
}



fn main() {
    println!("Hello, world!");
}
