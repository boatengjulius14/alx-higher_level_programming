#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to address of head
 * @number: number to inserted
 * Return: address of the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *temp, *add;
	node = malloc(sizeof(listint_t));

	if (!node)
		return (NULL);

	node->n = number;
	node->next = NULL;

	temp = *head;

	while (temp->n != 4)
		temp = temp->next;

	add = temp->next;

	temp->next = node;
	node->next = add;
	return (*head);
}
