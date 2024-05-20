.source ZCodeClass.java
.class public ZCodeClass
.super java.lang.Object

.method public <init>()V
Label0:
.var 0 is this LZCodeClass; from Label0 to Label1
	aload_0
	invokespecial java/lang/Object/<init>()V
	return
Label1:
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
	return
Label1:
.limit stack 0
.limit locals 0
.end method

.method public static main([Ljava/lang/String;)V
Label0:
.var 0 is args Ljava/lang/String; from Label0 to Label1
Label2:
.var 1 is i F from Label2 to Label3
	ldc 0.0000
	fstore_1
Label6:
	fload_1
	ldc 2.0000
	fcmpl
	iflt Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifgt Label8
	goto Label8
Label7:
	fload_1
	ldc 1.0000
	fadd
	fstore_1
	goto Label6
Label8:
Label3:
	return
Label1:
.limit stack 6
.limit locals 2
.end method
