#include "lists.h"

/**
 * reverselist - reverses a linked list
 * @mid: pointer to pointer to address of the first node
 */
void reverselist(listint_t **mid)
{
	listint_t *prev = NULL, *cur = *mid, *next = NULL;

	while (cur)
	{
		next = cur->next;
		cur->next = prev;
		prev = cur;
		cur = next;
	}
	*mid = prev;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to pointer to head
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *mid, *temp;

	if (!*head || !(*head)->next)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			mid = slow->next;
			break;
		}
		if (!fast->next)
		{
			mid = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverselist(&mid);
	temp = *head;

	while (mid)
	{
		if (temp->n == mid->n)
		{
			temp = temp->next;
			mid = mid->next;
			continue;
		}
		return (0);
	}
	return (1);
}
