
fn main() {
    let src = "
begin 644 root-me_challenge_uudeview
B5F5R>2!S:6UP;&4@.RD*4$%34R`](%5,5%)!4TE-4$Q%\"@``
`
end
";

    let lines : Vec<&str> = src.lines().collect();
    let start  = lines.iter().position(|l| l.starts_with("begin")).unwrap();
    let end = lines.iter().position(|l| l.starts_with("end")).unwrap();
    let data_lines : &[&str] = &lines[start+1..end];

    let mut dst: String = String::new();
    for line in data_lines {
        let vals = line[1..].chars().map(|v| v as u8).collect::<Vec<u8>>();
        for i in 0..vals.len()/4 {
            let u1 = (vals[i*4+0] - 32)%64; // Mod 64 to change backtick to space
            let u2 = (vals[i*4+1] - 32)%64;
            let u3 = (vals[i*4+2] - 32)%64;
            let u4 = (vals[i*4+3] - 32)%64;

            let v1 = (u1 << 2) + (u2 >> 4);
            let v2 = (u2 << 4) + (u3 >> 2);
            let v3 = (u3 << 6) + u4;

            dst.push(v1 as char);
            dst.push(v2 as char);
            dst.push(v3 as char);
        }
    }

    println!("Texte: {}", dst);
}
