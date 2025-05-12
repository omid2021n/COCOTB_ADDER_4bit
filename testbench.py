import cocotb
import random
from cocotb.triggers import Timer

@cocotb.test()
async def random_addition_test(dut):
    """Randomized test for the adder"""
    error_count = 0  # شمارنده خطاها
    total_tests = 20  # تعداد دفعات تست (میتونی اینو زیاد یا کم کنی)

    for i in range(10):  # Run 10 random tests
        # Generate random 4-bit numbers
        a = random.randint(0, 15)
        b = random.randint(0, 15)

        # Apply inputs
        dut.a.value = a
        dut.b.value = b

        # Wait for processing
        await Timer(10, units='ns')

        # Read the output
        y = dut.y.value.integer

        # Calculate expected value
        expected = a + b

        # Log the values
        dut._log.info(f"Test {i}: a={a}, b={b}, expected={expected}, got={y}")

        # Assertion
        #assert y == expected, f"Test {i} failed: {a} + {b} = {expected}, but DUT gave {y}"
         # بررسی و مدیریت خطا
        if y != expected:
            dut._log.error(f"❌ Test {i} FAILED: {a} + {b} = {expected}, but got {y}")
            error_count += 1

    # پایان تست - چاپ نتیجه نهایی
    if error_count == 0:
        dut._log.info(f"✅ All {total_tests} tests passed successfully!")
    else:
        dut._log.error(f"❌ {error_count} out of {total_tests} tests FAILED!")
        assert False, f"{error_count} tests failed!"

