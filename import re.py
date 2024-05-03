import re

def is_valid_scientific_number(number):
  """
  Fungsi ini memeriksa apakah string yang diberikan adalah scientific number yang valid.

  Args:
    number: String yang ingin diperiksa.

  Returns:
    True jika string adalah scientific number yang valid, False sebaliknya.
  """
  pattern = r"^-?\d+\.?\d*(?:e|E)[-+]?\d+$"
  match = re.match(pattern, number)
  return bool(match)

def main():
  """
  Fungsi utama untuk menjalankan program.
  """
  number = input("Masukkan scientific number: ")

  if is_valid_scientific_number(number):
    print(f"{number} adalah scientific number yang valid.")
  else:
    print(f"{number} bukan scientific number yang valid.")

if __name__ == "__main__":
  main()
