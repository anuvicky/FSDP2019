#include<stdio.h>
#include<stdlib.h>
void insertfirstnode();
void insertmiddlenode();
void insertlastnode();
void deletefirstnode();
void deletemiddlenode();
void deletelastnode();
void viewlist();
struct node
{
	int info;
	struct node *link;
};
struct node *start = NULL;

struct node *createnode()
{
	struct node *n;
	n =(struct node*)malloc(sizeof(struct node));
	return (n);
}
void insertfirstnode()
{
	struct node *temp,*t;
	temp = createnode();
	printf("enter a number");
	scanf("%d",&temp->info);
	temp->link = NULL;
	if( start == NULL)
	{
		start = temp;
	}
	else
	{
		t = start;
		start = NULL;
		start = temp;
		start->link = t;
	}
}
void insertmiddlenode()
{
	struct node *temp,*t;
	temp = createnode();
	printf("enter a number");
	scanf("%d",&temp->info);
	temp->link = NULL;
	if(start == NULL)
	{
		start = temp;
	}
	else
	{
		int n;
		t = start;
		printf("enter a number you put after the number will be addded ");
		scanf("%d",&n);
		while( t->info != n)
		{
			t = t->link;
		}
		temp->link= t->link;
		t->link = temp;
		
	}
}
void insertlastnode()
{
	struct node *temp, *t;
	temp = createnode();
	printf("enter a number");
	scanf("%d",&temp->info);
	temp->link=NULL;
	if(start == NULL)
	{
		start = temp;
	}
	else
	{
		t=start;
		while(t->link != NULL)
		{
			t = t->link;
			
		}
		t->link = temp;
	}
}
void deletefirstnode()
{
	struct node *r;
	if(start == NULL)
	{
		printf("list is empty");
	}
	else
	{
		r= start;
		start = start->link;
		free(r);
	}
}
void deletemiddlenode()
{
	struct node *r,*p;
	if( start == NULL)
	{
		printf("list is empty");
	}
	else
	{
		int n;
		printf("enter the number you want to delete ");
		scanf("%d",&n);
		r= start;
		while(r->info != n)
		{
			p = r;
			r = r->link;
		}
		if(r->link !=NULL)
		{
			p->link = r->link;
		    free(r);
		}
		else
		{
			printf("invalid postion unable to delete the node");
		}
		
	}
}
void deletelastnode()
{
	struct node *n,*p;
	if(start == NULL)
	{
		printf("list is empty");
		
	}
	else
	{
		n = start;
		while(n->link !=NULL)
		{
			p = n;
			n = n->link;
		}
		p->link = NULL;
		free(n);
	}
}
void viewlist()
{
	struct node *t;
	if(start == NULL)
	{
		printf("list is the empty");
	}
	else
	{
		t = start;
		while(t!= NULL)
		{
			printf("%d",t->info);
			t= t->link;
		}
	}
}
int menu()
{
	int ch;
	printf("\n1add the value in first node");
	printf("\n2add the value in the middle node");
	printf("\n3add the value in the last node");
	printf("\n4Delete the firstnode");
	printf("\n5Delete the middlenode");
	printf("\n6Delete the lastnode");
	printf("\n7traversing the node");
	printf("\n8Exist");
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
			case 1:insertfirstnode();
			        break;
			case 2:insertmiddlenode();
			        break;
			case 3:
			        insertlastnode();
			        break;
			case 4:
			        deletefirstnode();
			        break;
			case 5:
				    deletemiddlenode();
				    break;
			case 6:
				    deletelastnode();
				    break;
			case 7:
			        viewlist();
			        break;
			
			default:
			        printf("invalid choice");
			
		}
	}
}


















