
fn main() {
    let src = "436563692065737420756E6520706872617365207061722064656661757420706F75722063652070726F6A65742E204E6174";
    let mut dst: String = String::new();
    for i in (0..src.chars().count()).step_by(2) {
        dst.push(u8::from_str_radix(&src[i..i+2], 16).unwrap() as char);
    }

    println!("Texte: {}", dst);
}
