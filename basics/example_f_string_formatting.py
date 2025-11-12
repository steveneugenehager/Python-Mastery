
n = 1_234_567_890.12345
print("Format a large number with commas:" , n , '->' , f"{n:,}" )
print("Format a number with fixed precision:" , n , '->' , f"{n:.4f}" ,"(rounding for free)" )
print("Format a number with commas and fixed precision:" , n , '->' , f"{n:,.2f}" )
print("Format a number with explicit sign:" , n , '->' , f"{n:+}" )