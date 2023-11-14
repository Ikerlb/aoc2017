use std::io::{self, BufRead};

fn part1(mut a: i64, mut b: i64) -> usize {
    let modulo = (i32::MAX) as i64;
    let ma = 16807;
    let mb = 48271;

    let mask = (1 << 16) - 1;

    let mut res = 0;
    for i in 0..40000000 {
        a = (a * ma) % modulo;
        b = (b * mb) % modulo;
        if (a & mask) == (b & mask) {
            res += 1;
        }
    }
    return res;
}

fn step(mut prev: i64, base: i64, mult: i64, modulo: i64) -> i64 {
    let mask = (1 << 16) - 1;
    let mut nxt = (prev * base) % modulo;
    while (nxt % mult) != 0 {
        prev = nxt;
        nxt = (prev * base) % modulo;
    }
    return nxt;
}

fn part2(mut a: i64, mut b: i64) -> usize {
    let ma = 16807;
    let mb = 48271;

    let modulo = (i32::MAX) as i64;
    let mask = (1 << 16) - 1;

    let mut res = 0;

    for i in 0..5000000 {
        a = step(a, ma, 4, modulo);
        b = step(b, mb, 8, modulo);
        if (a & mask) == (b & mask) {
            res += 1;
        }
    }
    return res;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res_s| {
            let s = res_s.unwrap();
            let mut binding = s.split(" ");
            let last = binding.last().unwrap();
            return last.parse::<i64>().unwrap()
        });


    let mut a = lines.next().unwrap();
    let mut b = lines.next().unwrap();

        
    println!("{}", part1(a, b));
    println!("{}", part2(a, b));

    Ok(())
}


