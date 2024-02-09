int getAverage(List<int> arr) {
  return arr.reduce((value, element) => value + element) ~/ arr.length;
}

void main(List<String> args) {
  print(getAverage([8, 20, 12, 7, 8, 14, 16, 1, 2, 17]));
}
