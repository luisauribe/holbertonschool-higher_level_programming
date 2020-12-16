#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: Pointer to the head.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 **/
int is_palindrome(listint_t **head)
{
	listint_t *run2 = *head;
	int i = 0, z = 0, list[8192];

	if (head == NULL || *head == NULL)
	{
		return (1);
	}

	while (run2)
	{
		list[i] = run2->n;
		run2 = run2->next;
		i++;
	}
	for (; i > 0; i--)
	{
		if (list[z] != list[i - 1])
		{
			return (0);
		}
		z++;
	}
	return (1);
}
