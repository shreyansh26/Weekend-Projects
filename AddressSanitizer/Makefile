run:
	g++ -O -g -fsanitize=address heap_use_after_free.cpp -o heap_use_after_free
	g++ -O -g -fsanitize=address heap_buffer_overflow.cpp -o heap_buffer_overflow
	g++ -O -g -fsanitize=address stack_buffer_overflow.cpp -o stack_buffer_overflow
	g++ -O -g -fsanitize=address global_buffer_overflow.cpp -o global_buffer_overflow
clean:
	rm heap_use_after_free heap_buffer_overflow stack_buffer_overflow global_buffer_overflow
