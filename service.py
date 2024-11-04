from model import session, User, Contact


def add_contact_service(owner_name, name, phone_number, email):

    try:
        # print('service: ', owner_name, name, phone_number, email)

        if owner_name and name and phone_number:

            owner_user = session.query(User).filter_by(name=owner_name).first()

            if not owner_user:
                owner_user = User(name=owner_name)
                session.add(owner_user)
                session.commit()

            existing_contact = session.query(Contact).filter_by(phone_number=phone_number,
                                                                owner_user_id=owner_user.id
                                                                ).first()
            if existing_contact:
                return "Contact Already Exists"

            contact = Contact(name=name,
                              phone_number=phone_number,
                              email=email,
                              owner_user_id=owner_user.id)

            session.add(contact)
            session.commit()

            return "A new contact has been added"

    except Exception as e:
        session.rollback()
        raise Exception(f"Error Happened in adding contact: {e}")

    finally:
        session.close()


def get_contacts_service(owner_name):

    try:
        owner_user = session.query(User).filter_by(name=owner_name).first()
        contacts = session.query(Contact).filter_by(
            owner_user_id=owner_user.id).all()

        if not owner_name and not contacts:
            return []

        # print('Contacts:', contacts[0].name, contacts[1].name)

        return contacts

    except Exception as e:
        print(f"Error in getting contacts: {e}")
        return []

    finally:
        session.close()


def edit_contact_service(owner_name, old_contact_name, new_contact_name, new_phone, new_email):

    try:
        owner_user = session.query(User).filter_by(name=owner_name).first()
        contact = session.query(Contact).filter_by(
            name=old_contact_name, owner_user_id=owner_user.id).first()

        if not owner_user and not contact:
            return "No contact found to update"

        contact.name = new_contact_name
        contact.phone_number = new_phone
        contact.email = new_email
        session.commit()

        return "Contact has been updated Successfully"

    except:
        session.rollback()
        return "Error in updating contacts may be contact is not found"
    finally:
        session.close()


def remove_contact_service(owner_name, contact_name):

    try:
        owner_user = session.query(User).filter_by(name=owner_name).first()
        contact = session.query(Contact).filter_by(
            name=contact_name, owner_user_id=owner_user.id).first()

        if not contact:
            return "No Contact Found to delete"

        session.delete(contact)
        session.commit()
        return "Contact is deleted"

    except Exception as e:
        session.rollback()
        raise Exception(f"Error in deleting contact {e}")
    finally:
        session.close()
