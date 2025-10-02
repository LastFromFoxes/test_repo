use std::io;

fn main() {
    println!("Введите ваше имя:");

    // читаем строку из stdin
    let mut name = String::new();
    io::stdin()
        .read_line(&mut name)
        .expect("Не удалось прочитать строку");

    let name = name.trim(); // убираем \n

    println!("Привет, {}!", name);

    // простая функция сложения
    let a = 1;
    let b = 4;
    println!("{} + {} = {}", a, b, add(a, b));
}

// отдельная функция
fn add(x: i32, y: i32) -> i32 {
    x + y
}
