

#[cfg(test)]
mod tests {
	use crate::*;
	
	fn t(root: Option<Rc<RefCell<TreeNode>>>, expected: Option<Rc<RefCell<TreeNode>>>) {
		let result = Solution::bst_to_gst(root);
		println!("{:?}", result);
		// assert_eq!(result, expected);
	}
	
	#[test]
	fn test1() {
		// root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
		// replace null with -1
		let v = vec![4,1,6,0,2,5,7,-1,-1,-1,3,-1,-1,-1,8];
		let root = helper(v);
		t(root, None);
	}

	#[test]
	fn test2() {
		// root = [0,null,1]
		let v = vec![0,-1,1];
		let root = helper(v);
		t(root, None);
	}

}