impl Solution {
    pub fn count_symmetric_integers(low: i32, high: i32) -> i32 {
        let mut t = 0;
        for i in low..=high {
            let s: String = i.to_string();

            let n = s.len();
            if n % 2 != 0 {
                continue
            }

            let mut a = 0;
            let mut b = 0;
            let half = n / 2;

            // Convert the string to bytes for fast ASCII indexing
            let bytes = s.as_bytes();

            // 2. Sum the first half
            for m in 0..half {
                a += (bytes[m] - b'0') as i32; 
            }

            // 3. Example: Sum the second half (if that is your next step)
            for m in half..(half * 2) {
                b += (bytes[m] - b'0') as i32;
            }

            if a == b {
                t += 1
            }
        }

        t
    }
}