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
	ldc 2.0000
	ldc 2.0000
	fcmpl
	ifeq Label6
	iconst_0
	goto Label7
Label6:
	iconst_1
Label7:
	ifle Label8
	ldc 1.0000
	invokestatic io/writeNumber(F)V
	goto Label9
Label10:
	goto Label9
Label8:
Label9:
Label3:
	return
Label1:
.limit stack 3
.limit locals 1
.end method
