#include "lists.h"
#include <stdlib.h>

/**
* palindrome - Function to help and verify the palindrome list
* @head: head of the list
* @temp: last of the list
* @len: length of the list
* Return: the correct value of each case: 0 not, 1 yes
*/

int palindrome(listint_t *head, listint_t *temp, int len)
{
	listint_t *help = head;
	int i = 0;

	if (len <= 1)
		return (1);
	else if (head->n == temp->n)
	{
		while (i < len - 1)
		{
			help = help->next;
			i++;
		}
		return (palindrome(head->next, help, len - 3));
	}
	else
		return (0);
}

/**
* is_palindrome - Function that checks if a singly linked list is a palindrome.
* @head: head of the list.
* Return: 0 if it is not a palindrome, else 1
*/

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int len = 0, i = 0;

	if (head == NULL)
		return (1);

	temp = *head;
	while (temp != NULL)
	{
		temp = temp->next;
		len++;
	}
	temp = *head;
	while (i < len - 1)
	{
		temp = temp->next;
		i++;
	}
	return (palindrome(*head, temp, len));
}
