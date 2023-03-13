#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int count = 0, i = 0;
	listint_t *temp;

	if (!*head)
		return (1);

	temp = *head;
	while (temp)
	{
		count++;
		temp = temp->next;
	}

	int store[count];

	temp = *head;

	while (i < count)
	{
		store[i] = temp->n;
		temp = temp->next;
		i++;
	}

	i = 0;
	while (i < (count / 2))
	{
		if (store[i] == store[count - i - 1])
		{
			i++;
			continue;
		}
		return (0);
	}
	return (1);
}
