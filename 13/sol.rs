use std::io::{self, BufRead};

fn severity(v: &Vec<(usize, usize)>, delay: usize) -> Option<usize> {
    let mut s = 0;
    let mut avoids = true;
    for &(d, r) in v {
        if (d + delay) % (r + r - 2) == 0 {
            avoids = false;
            s += d * r;
        }
    }
    if avoids {
        return None;
    } else {
        return Some(s);
    }
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let v = stdin
        .lock()
        .lines()
        .map(|res_s| {
            let s = res_s.unwrap();
            let mut binding = s.split(": ");
            let range = binding.next().unwrap().parse::<usize>().unwrap();
            let depth = binding.next().unwrap().parse::<usize>().unwrap();
            return (range, depth);
        }).collect::<Vec<_>>();

    let s = severity(&v, 0).unwrap();
    println!("{}", s);

    let mut i = 0;
    while let Some(sev) = severity(&v, i) {
        i += 1;
    }
    println!("{}", i);


    Ok(())    
}


