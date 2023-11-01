#include <stdio.h>

int main()
{
    int input;
    printf("Enter a number : \n");
    scanf("%d", &input);
    if (input % 2 == 0)
    {
        printf("Number is even\n");
    }
    else
    {
        printf("Number is odd \n");
    }
    return 0;

}