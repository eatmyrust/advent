use std::fs;

fn main() {
    let file_contents = fs::read_to_string("inputs/day_1.txt")
    .expect("Should have been able to read the file.");

    let lines = file_contents.split("\n\n");
    let lines_vec: Vec<&str> = lines.collect();
    let mut added_cals: Vec<i32> = vec![];
    for line in lines_vec {
        let mut total = 0;
        let calories = line.lines();
        let calories_vec: Vec<&str> = calories.collect();

        for calorie in calories_vec{
            total = total + calorie.parse::<i32>().unwrap();
        }
        added_cals.push(total);
    }
    let max_cals = added_cals.iter().max().cloned().unwrap();
    added_cals.sort();
    let top_three = added_cals.pop().unwrap() + added_cals.pop().unwrap() + added_cals.pop().unwrap();
    println!("{}, {}", max_cals, top_three)
}