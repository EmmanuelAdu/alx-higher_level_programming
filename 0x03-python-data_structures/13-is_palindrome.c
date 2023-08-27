#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - this function checks if a list is a palindrome
 * @head: POINTER TO THE FIRST NODE OF LIST
 * Return: 1 on success else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *tempPtr, *revPtr;
	listint_t *midPtr;
	int i, len = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	tempPtr = *head;
	while (tempPtr != NULL)
	{
		tempPtr = tempPtr->next;
		len++;
	}
	tempPtr = *head;
	for (i = 0; i < (len / 2) - 1; i++)
		tempPtr = tempPtr->next;
	if (len % 2 == 0 && tempPtr->n != tempPtr->next->n) /* if even */
		return (0);
	tempPtr = tempPtr->next->next;
	revPtr = reverse_list(&tempPtr);
	midPtr = revPtr;
	tempPtr = *head;
	while (revPtr)
	{
		if (tempPtr->n != revPtr->n)
			return (0);
		tempPtr = tempPtr->next;
		revPtr = revPtr->next;
	}
	reverse_list(&midPtr);
	return (1);
}

/**
 * reverse_list - This function reverse the pointing direction of a list
 * @head: pointer to the first node of list
 * Return: the address of the head node of the list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *firstnode, *prevnode, *nextnode;

	firstnode = *head;
	prevnode = NULL;
	while (firstnode)
	{
		nextnode = firstnode->next;
		firstnode->next = prevnode;
		prevnode = firstnode;
		firstnode = nextnode;
	}
	*head = prevnode;
	return (*head);
}
