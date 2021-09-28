.data
list: .space 44
newline: .asciiz "\n"
.text
addi $t0, $zero, 0
addi $s0, $zero, 1
sw $s0, list($t0)
addi $t0, $t0, 4
addi $s0, $zero, 2
sw $s0, list($t0)
addi $t0, $t0, 4
addi $s0, $zero, 3
sw $s0, list($t0)
addi $t0, $t0, 4
addi $s0, $zero, 4
sw $s0, list($t0)
addi $t0, $t0, 4
addi $s0, $zero, 5
sw $s0, list($t0)
addi $t0, $t0, 4
addi $s0, $zero, 6
sw $s0, list($t0)
addi $t0, $t0, 4
addi $s0, $zero, 7
sw $s0, list($t0)
addi $t0, $t0, 4
addi $s0, $zero, 8
sw $s0, list($t0)
addi $t0, $t0, 4
addi $s0, $zero, 9
sw $s0, list($t0)
addi $t0, $t0, 4
addi $s0, $zero, 10
sw $s0, list($t0)
addi $t0, $t0, 4
j main
func:
slt $t2, $s2, $s3
beq $t2, $zero, exit
move $s7, $s3
mul $s6, $s7, 4
j loop
loop:
beq $s7, $zero, print
mul $s2, $s2, 2
add $s2, $s2, 1
move $s0, $s2
sw $s0, list($s6)
sub $s7, $s7, 1
sub $s6, $s6, 4
j loop
print:
mul $s3, $s3, 4
lw $t6, list($s3)
li $v0, 1
move $a0, $t6
syscall
li $v0, 4
la $a0, newline
syscall
jr $ra
exit:
li $v0, 1
li $a0, 0
syscall
li $v0, 4
la $a0, newline
syscall
jr $ra
write:
addi $s1, $ra, 0
jal func
move $ra, $s1
jr $ra
main:
li $s2, 5
li $s3, 10
jal write
li $s2, 10
li $s3, 5
jal write
li $v0, 10
syscall
