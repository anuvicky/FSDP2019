#include<stdio.h>
#include<stdlib.h>
struct node
{
	int info;
	struct node *prev , *next;
};
struct node *start = NULL;
void insertatbegin()
{
	struct node *n,*temp;
	n = (struct node *)malloc(sizeof(struct node));

	printf("enter a  number");
	scanf("%d",&n->info);
	n->prev = NULL;
	n->next = NULL;
	if(start == NULL)
	{
		start = n;
	}
	else
	{
		temp = start;
		start->prev = n;
		n->next = temp;
		start =n; 
		
	}
}
void deletefirstnode()
{
	struct node *temp;
	if(start == NULL)
	{
		printf("list is empty");
	}
	else
	{
		temp= start;
		start = start->next;
	/*	start->prev = NULL; problem is that if i am using this statement then whike loop have completed without using exist */ 

		free(temp);
	}
	
}
void traversing()
{
	struct node *t;
	if(start == NULL)
	{
		printf("list is empty");
	}
	else
	{
		t= start;
		while(t !=NULL)
		{
			printf("%d",t->info);
			t = t->next;
		}
	}	
}
int menu()
{
	int ch;
	printf("\n1add the value first node");
	printf("\n2delete the first node");
	printf("\n3traversing the node");
	printf("\nenter your choice");
	scanf("%d",&ch);
	return (ch);
}
int main()
{
	while(1)
	{
		switch(menu())
		{
			case 1:
			    insertatbegin();
			    break;
			case 2:
				deletefirstnode();
				break;
			case 3:
				traversing();
				break;
			default:
				printf("invalid output");
		}
	}
}












